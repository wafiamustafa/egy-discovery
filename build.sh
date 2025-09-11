#!/bin/bash
echo \"Building frontend for Vercel deployment...\"
cd frontend
npm ci
npm run build
echo \"Frontend build complete!\"
ls -la dist/