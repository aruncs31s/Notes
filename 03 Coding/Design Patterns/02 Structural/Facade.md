---
id: Facade
aliases: []
tags:
  - coding
  - design_patterns
  - structural
dg-publish: true
---
# Facade Pattern

## Without Facade

```ts
const paymentProc = new PaymentProcessor();
const inventorySystem = new InventorySystem();
const shippingService = new ShippingService();
const fraudDetection = new FraudDetection();

if (fraudChecker.verify(user)){
    if (inventorySystem.checkStock(item)){
        paymentProc.processPayment(user, item);
        inventorySystem.updateStock(item);
        shippingService.shipItem(user, item);
    } else {
        console.log("Item out of stock");
    }
}

```

### Without Facade in Go

```go
package main
import "fmt"
type PaymentProcessor struct{}
func (p *PaymentProcessor) ProcessPayment(user User, item Item) {
    fmt.Println("Processing payment for", user.Name, "for item", item.Name)
}
type InventorySystem struct{}
func (i *InventorySystem) CheckStock(item Item) bool {
    fmt.Println("Checking stock for item", item.Name)
    return true // Assume item is in stock
}
func (i *InventorySystem) UpdateStock(item Item) {
    fmt.Println("Updating stock for item", item.Name)
}
type ShippingService struct{}
func (s *ShippingService) ShipItem(user User, item Item) {
    fmt.Println("Shipping item", item.Name, "to", user.Address)
}
type FraudDetection struct{}
func (f *FraudDetection) Verify(user User) bool {
    fmt.Println("Verifying user", user.Name)
    return true // Assume user is verified
}
type User struct {
    Name    string
    Address string
}
type Item struct {
    Name string
}
func main() {
    user := User{Name: "Alice", Address: "123 Main St"}
    item := Item{Name: "Laptop"}
    paymentProc := &PaymentProcessor{}
    inventorySystem := &InventorySystem{}
    shippingService := &ShippingService{}
    fraudDetection := &FraudDetection{}
    if fraudDetection.Verify(user) {
        if inventorySystem.CheckStock(item) {
            paymentProc.ProcessPayment(user, item)
            inventorySystem.UpdateStock(item)
            shippingService.ShipItem(user, item)
        } else {
            fmt.Println("Item out of stock")
        }
    }
}

```

## With Facade

```ts
const orderSystem = new OrderFacade();
orderSystem.placeOrder(user, item);

```

### With Facade in Go 

```go
package main
import "fmt"
type OrderFacade struct {
    paymentProcessor PaymentProcessor
    inventorySystem  InventorySystem
    shippingService  ShippingService
    fraudDetection   FraudDetection
}
func NewOrderFacade() *OrderFacade {
    return &OrderFacade{
        paymentProcessor: NewPaymentProcessor(),
        inventorySystem:  NewInventorySystem(),
        shippingService:  NewShippingService(),
        fraudDetection:   NewFraudDetection(),
    }
}
}
func (f *OrderFacade) PlaceOrder(user User, item Item) {
    if f.fraudDetection.Verify(user) {
        if f.inventorySystem.CheckStock(item) {
            f.paymentProcessor.ProcessPayment(user, item)
            f.inventorySystem.UpdateStock(item)
            f.shippingService.ShipItem(user, item)
        } else {
            fmt.Println("Item out of stock")
        }
    }
}

```

