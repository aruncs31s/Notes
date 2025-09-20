---
id: ESP-CSI
aliases: []
tags:
  - electronics
  - embedded_systems
  - micro_controllers
  - espressif
  - esp32
dg-publish: true
---
# ESP-CSI

<!-- HACK: -->

```c
#include <stdio.h>
#include <math.h>
#include "esp_wifi.h"
#include "esp_system.h"

void csi_callback(void *ctx, wifi_csi_info_t *info) {
    int16_t *csi_data = info->buf;
    int len = info->len;

    for (int i = 0; i < len / 2; i++) {
        int16_t real = csi_data[2 * i];
        int16_t imag = csi_data[2 * i + 1];

        // Calculate amplitude and phase
        float amplitude = sqrt(real * real + imag * imag);
        float phase = atan2(imag, real);

        printf("Subcarrier %d: Amplitude: %.2f, Phase: %.2f\n", i + 1, amplitude, phase);
    }
}

void app_main() {
    esp_wifi_set_csi_rx_cb(csi_callback, NULL);
}

```
