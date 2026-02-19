#!/usr/bin/env node
const { execSync } = require('child_process');

function build() {
    try {
        execSync('tsc && npm test', { stdio: 'inherit' });
        return 0;
    } catch (error) {
        return error.status || 1;
    }
}

process.exit(build());
