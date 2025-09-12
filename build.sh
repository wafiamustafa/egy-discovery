#!/bin/bash
echo "Building frontend for Vercel deployment..."
cd frontend
npm ci
npm run build
echo "Frontend build complete!"
ls -la dist/

# Copy built assets to project root for Vercel static serving
echo "Copying assets to project root..."
cd ..
cp -r frontend/dist/* .
echo "Assets copied successfully!"
ls -la assets/