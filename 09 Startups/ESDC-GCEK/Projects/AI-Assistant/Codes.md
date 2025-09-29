---
id: Codes
aliases: []
tags: []
---

```python


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--run':
          start_all_servers()
        elif sys.argv[1] == '--test':
          # test_api_endpoints()
          pass
        elif sys.argv[1] == '--guide':
          pass
        else:
            print("Usage:")
            print("  python launcher.py --run  # Start all servers")
            print("  python launcher.py --test # Test API endpoints")
    else:
        try:
            start_all_servers()
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
```
