---
id: esp_mesh
aliases: []
tags:
  - projects
  - electronics
  - node_to_node_communication
dg-publish: true
---
2. OnReceive() callback function

```c
void espMesh::mesh::OnReceive(const uint8_t *mac_addr,
                              const uint8_t *incomingData, int len) {
  char macStr[18];
  Serial.print("Packet received from: ");
  snprintf(macStr, sizeof(macStr), "%02x:%02x:%02x:%02x:%02x:%02x", mac_addr[0],
           mac_addr[1], mac_addr[2], mac_addr[3], mac_addr[4], mac_addr[5]);
  Serial.println(macStr);
  memcpy(&Message_ptr, incomingData, sizeof(Message_ptr));
  Serial.printf("Board ID %u: %u bytes\n", Message_ptr->UID, len);
}

```
