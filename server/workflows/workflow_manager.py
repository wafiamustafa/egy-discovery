#!/usr/bin/env python3
"""
Workflow Manager Utility

A utility script for managing N8N and Zapier workflows in the workflows directory.
"""

import os
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

class WorkflowManager:
    """Manages workflow files in the workflows directory"""
    
    def __init__(self, workflows_dir: str = "server/workflows"):
        self.workflows_dir = Path(workflows_dir)
        self.n8n_dir = self.workflows_dir / "n8n"
        self.zapier_dir = self.workflows_dir / "zapier"
        self.examples_dir = self.workflows_dir / "examples"
        
        # Ensure directories exist
        self.n8n_dir.mkdir(parents=True, exist_ok=True)
        self.zapier_dir.mkdir(parents=True, exist_ok=True)
        self.examples_dir.mkdir(parents=True, exist_ok=True)
    
    def list_workflows(self, platform: str = None) -> Dict[str, List[Dict[str, Any]]]:
        """List all workflows, optionally filtered by platform"""
        workflows = {
            "n8n": [],
            "zapier": [],
            "examples": []
        }
        
        # Scan N8N workflows
        for file_path in self.n8n_dir.glob("*.json"):
            try:
                with open(file_path, 'r') as f:
                    workflow_data = json.load(f)
                    workflows["n8n"].append({
                        "filename": file_path.name,
                        "name": workflow_data.get("name", "Unknown"),
                        "version": workflow_data.get("versionId", "Unknown"),
                        "tags": workflow_data.get("tags", []),
                        "active": workflow_data.get("active", False),
                        "size": file_path.stat().st_size
                    })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        
        # Scan Zapier workflows
        for file_path in self.zapier_dir.glob("*.json"):
            try:
                with open(file_path, 'r') as f:
                    workflow_data = json.load(f)
                    zap_data = workflow_data.get("zap", {})
                    workflows["zapier"].append({
                        "filename": file_path.name,
                        "name": zap_data.get("name", "Unknown"),
                        "version": zap_data.get("version", "Unknown"),
                        "tags": zap_data.get("tags", []),
                        "status": zap_data.get("status", "Unknown"),
                        "size": file_path.stat().st_size
                    })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        
        # Scan example files
        for file_path in self.examples_dir.glob("*.json"):
            try:
                with open(file_path, 'r') as f:
                    workflow_data = json.load(f)
                    workflows["examples"].append({
                        "filename": file_path.name,
                        "name": workflow_data.get("name", "Unknown"),
                        "description": workflow_data.get("description", "No description"),
                        "version": workflow_data.get("version", "Unknown"),
                        "size": file_path.stat().st_size
                    })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        
        if platform:
            return {platform: workflows.get(platform, [])}
        return workflows
    
    def validate_workflow(self, file_path: Path) -> Dict[str, Any]:
        """Validate a workflow file"""
        try:
            with open(file_path, 'r') as f:
                workflow_data = json.load(f)
            
            validation_result = {
                "valid": True,
                "errors": [],
                "warnings": [],
                "file_path": str(file_path),
                "file_size": file_path.stat().st_size
            }
            
            # Basic JSON validation
            if not isinstance(workflow_data, dict):
                validation_result["valid"] = False
                validation_result["errors"].append("Root must be a JSON object")
                return validation_result
            
            # Platform-specific validation
            if "zap" in workflow_data:
                # Zapier workflow
                zap_data = workflow_data["zap"]
                required_fields = ["id", "name", "triggers", "actions"]
                for field in required_fields:
                    if field not in zap_data:
                        validation_result["warnings"].append(f"Missing field: {field}")
                
                if not zap_data.get("triggers"):
                    validation_result["warnings"].append("No triggers defined")
                if not zap_data.get("actions"):
                    validation_result["warnings"].append("No actions defined")
                    
            elif "nodes" in workflow_data:
                # N8N workflow
                if not workflow_data.get("nodes"):
                    validation_result["warnings"].append("No nodes defined")
                if not workflow_data.get("connections"):
                    validation_result["warnings"].append("No connections defined")
                    
            else:
                validation_result["warnings"].append("Unknown workflow format")
            
            return validation_result
            
        except json.JSONDecodeError as e:
            return {
                "valid": False,
                "errors": [f"Invalid JSON: {e}"],
                "warnings": [],
                "file_path": str(file_path),
                "file_size": file_path.stat().st_size if file_path.exists() else 0
            }
        except Exception as e:
            return {
                "valid": False,
                "errors": [f"Error reading file: {e}"],
                "warnings": [],
                "file_path": str(file_path),
                "file_size": file_path.stat().st_size if file_path.exists() else 0
            }
    
    def validate_all_workflows(self) -> Dict[str, List[Dict[str, Any]]]:
        """Validate all workflow files"""
        validation_results = {
            "n8n": [],
            "zapier": [],
            "examples": []
        }
        
        # Validate N8N workflows
        for file_path in self.n8n_dir.glob("*.json"):
            validation_results["n8n"].append(self.validate_workflow(file_path))
        
        # Validate Zapier workflows
        for file_path in self.zapier_dir.glob("*.json"):
            validation_results["zapier"].append(self.validate_workflow(file_path))
        
        # Validate example files
        for file_path in self.examples_dir.glob("*.json"):
            validation_results["examples"].append(self.validate_workflow(file_path))
        
        return validation_results
    
    def create_workflow_from_template(self, platform: str, name: str, description: str = "") -> str:
        """Create a new workflow from template"""
        if platform not in ["n8n", "zapier"]:
            raise ValueError("Platform must be 'n8n' or 'zapier'")
        
        # Load template
        template_path = self.examples_dir / "workflow-template.json"
        if not template_path.exists():
            raise FileNotFoundError("Template file not found")
        
        with open(template_path, 'r') as f:
            template = json.load(f)
        
        # Customize template
        timestamp = datetime.now().isoformat() + "Z"
        template["name"] = name
        template["description"] = description
        template["created_at"] = timestamp
        template["updated_at"] = timestamp
        template["author"] = "Generated by WorkflowManager"
        
        # Create filename
        filename = f"{name.lower().replace(' ', '-')}-v1.0.json"
        file_path = self.workflows_dir / platform / filename
        
        # Write workflow file
        with open(file_path, 'w') as f:
            json.dump(template, f, indent=2)
        
        return str(file_path)
    
    def get_workflow_stats(self) -> Dict[str, Any]:
        """Get statistics about workflows"""
        stats = {
            "total_files": 0,
            "total_size": 0,
            "by_platform": {
                "n8n": {"count": 0, "size": 0},
                "zapier": {"count": 0, "size": 0},
                "examples": {"count": 0, "size": 0}
            }
        }
        
        for platform in ["n8n", "zapier", "examples"]:
            platform_dir = self.workflows_dir / platform
            if platform_dir.exists():
                for file_path in platform_dir.glob("*.json"):
                    stats["total_files"] += 1
                    file_size = file_path.stat().st_size
                    stats["total_size"] += file_size
                    stats["by_platform"][platform]["count"] += 1
                    stats["by_platform"][platform]["size"] += file_size
        
        return stats

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(description="Workflow Manager Utility")
    parser.add_argument("--list", action="store_true", help="List all workflows")
    parser.add_argument("--validate", action="store_true", help="Validate all workflows")
    parser.add_argument("--stats", action="store_true", help="Show workflow statistics")
    parser.add_argument("--platform", choices=["n8n", "zapier", "examples"], help="Filter by platform")
    parser.add_argument("--create", metavar="NAME", help="Create new workflow from template")
    parser.add_argument("--description", metavar="DESC", help="Description for new workflow")
    
    args = parser.parse_args()
    
    manager = WorkflowManager()
    
    if args.list:
        workflows = manager.list_workflows(args.platform)
        for platform, workflow_list in workflows.items():
            if workflow_list:
                print(f"\n{platform.upper()} Workflows:")
                print("-" * 50)
                for workflow in workflow_list:
                    print(f"  {workflow['filename']}")
                    print(f"    Name: {workflow['name']}")
                    if 'version' in workflow:
                        print(f"    Version: {workflow['version']}")
                    if 'tags' in workflow and workflow['tags']:
                        print(f"    Tags: {', '.join(workflow['tags'])}")
                    if 'description' in workflow:
                        print(f"    Description: {workflow['description']}")
                    print(f"    Size: {workflow['size']} bytes")
                    print()
    
    elif args.validate:
        results = manager.validate_all_workflows()
        for platform, validations in results.items():
            if validations:
                print(f"\n{platform.upper()} Validation Results:")
                print("-" * 50)
                for result in validations:
                    status = "✅ VALID" if result["valid"] else "❌ INVALID"
                    print(f"  {result['file_path']}: {status}")
                    if result["errors"]:
                        for error in result["errors"]:
                            print(f"    Error: {error}")
                    if result["warnings"]:
                        for warning in result["warnings"]:
                            print(f"    Warning: {warning}")
                    print()
    
    elif args.stats:
        stats = manager.get_workflow_stats()
        print("\nWorkflow Statistics:")
        print("-" * 30)
        print(f"Total files: {stats['total_files']}")
        print(f"Total size: {stats['total_size']} bytes ({stats['total_size'] / 1024:.1f} KB)")
        print("\nBy Platform:")
        for platform, data in stats["by_platform"].items():
            if data["count"] > 0:
                print(f"  {platform}: {data['count']} files, {data['size']} bytes")
    
    elif args.create:
        if not args.platform:
            print("Error: --platform is required when creating a workflow")
            return
        
        try:
            file_path = manager.create_workflow_from_template(
                args.platform, 
                args.create, 
                args.description or ""
            )
            print(f"Created workflow: {file_path}")
        except Exception as e:
            print(f"Error creating workflow: {e}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
