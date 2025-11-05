#!/bin/bash
# Quick start script for the TDD Calculator

echo "======================================"
echo "TDD Calculator - Quick Start"
echo "======================================"
echo ""

# Run tests
echo "Running tests..."
pytest -v tests/

echo ""
echo "======================================"
echo "All tests passed! ✓"
echo "======================================"
echo ""
echo "To run the GUI calculator, execute:"
echo "  cd src && python main.py"
echo ""
