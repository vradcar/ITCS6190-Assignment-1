#!/bin/bash
# Simple script to manage the docker containers

# Display help message
show_help() {
  echo "Usage: ./run.sh [command]"
  echo ""
  echo "Commands:"
  echo "  build   Build the app container"
  echo "  up      Start all services"
  echo "  down    Stop all services"
  echo "  clean   Remove output files and stop services"
  echo "  help    Show this help message"
  echo ""
}

# Handle commands
case "$1" in
  build)
    docker compose build app
    ;;
  up)
    docker compose up --build
    ;;
  down)
    docker compose down -v
    ;;
  clean)
    docker compose down -v
    rm -rf out
    mkdir -p out
    echo "Cleaned output directory"
    ;;
  *)
    show_help
    ;;
esac
