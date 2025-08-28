# Workflows Directory

This directory contains workflow definitions for various automation platforms including N8N and Zapier.

## Directory Structure

```
workflows/
├── n8n/           # N8N workflow JSON files
├── zapier/        # Zapier workflow JSON files  
├── examples/      # Example workflow templates
└── README.md      # This file
```

## Workflow Types

### N8N Workflows (`n8n/`)
- **Format**: JSON files with `.json` extension
- **Naming**: `{workflow-name}-{version}.json`
- **Example**: `email-notification-v1.0.json`

### Zapier Workflows (`zapier/`)
- **Format**: JSON files with `.json` extension
- **Naming**: `{zap-name}-{version}.json`
- **Example**: `slack-notification-v1.0.json`

## Usage

### Importing Workflows
Workflows can be imported into their respective platforms:

**N8N:**
1. Copy the JSON content from the workflow file
2. In N8N, go to Workflows → Import from URL/File
3. Paste the JSON content
4. Save and activate the workflow

**Zapier:**
1. Use the Zapier CLI: `zapier import {workflow-file}`
2. Or manually recreate the workflow using the JSON as a reference

### Workflow Management
- Keep workflow versions in separate files
- Document any dependencies or prerequisites
- Include workflow descriptions in the JSON metadata
- Test workflows before committing to this repository

## Best Practices

1. **Versioning**: Use semantic versioning (e.g., v1.0.0, v1.1.0)
2. **Documentation**: Include clear descriptions and usage instructions
3. **Testing**: Test workflows in development environments first
4. **Backup**: Keep backups of production workflows
5. **Security**: Never commit sensitive credentials or API keys

## Example Workflows

See the `examples/` directory for sample workflow templates that can be customized for your needs.
