set -euo pipefail

# Default values (optional)
a="5"
b="10"

# Parse named arguments
while [[ "$#" -gt 0 ]]; do
    case "$1" in
        --a)
            a="$2"
            shift 2
            ;;
        --b)
            b="$2" shift 2
            ;;
        *)
            echo "Unknown parameter passed: $1"
            exit 1
            ;;
    esac
done

# Validate integers
if ! [[ "$a" =~ ^-?[0-9]+$ ]]; then
    echo "Error: --a must be an integer"
    exit 1
fi

if ! [[ "$b" =~ ^-?[0-9]+$ ]]; then
    echo "Error: --b must be an integer"
    exit 1
fi


S=http://127.0.0.1:8080/mcp/
ACCEPT='application/json, text/event-stream'
CT='application/json'

curl -sS -X POST $S \
  -H "Accept: $ACCEPT" \
  -H "Content-Type: $CT" \
  -X POST "$S" \
  -d "$(cat <<EOF
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "add",
    "arguments": {
      "a": $a,
      "b": $b
    }
  }
}
EOF
)"
