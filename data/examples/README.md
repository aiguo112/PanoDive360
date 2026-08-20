# Example subset

These six ERP stills and RGB masks are a **sample only**. The full PanoDive360 set has 1,052 labeled frames and is not stored in git.

```text
data/examples/
  images/    # RGB equirectangular stills
  masks/     # pixel labels, same stem, PNG
```

| File | Classes visible in the mask |
| --- | --- |
| `initial_360-ERP_417` | diver, shipwreck |
| `initial_360-ERP_1035` | diver, fish, dolphin, coral, seaweed |
| `initial_360-ERP_1074` | diver, shark, fish |
| `initial_360-ERP_1114` | diver, coral, seaweed |
| `initial_360-ERP_185` | diver, shark |
| `initial_360-ERP_0` | diver, dolphin, seaweed |

Training still expects the split layout under `data/splits/` (or `PANODIVE360_DATA`). You can copy this example folder there to smoke-test the loader.
