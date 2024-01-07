class SmartContract:
    # Represents a simple smart contract for an e-commerce transaction
    def __init__(self):
        # Initialize the contract with default values
        self.buyer = None
        self.seller = None
        self.price = 0
        self.buyer_paid = False
        self.item_delivered = False

    def initiate_contract(self, buyer, seller, price):
        # Initiates the contract with buyer, seller, and price details
        # Only allows initiation if contract hasn't been set up yet
        if not self.buyer and not self.seller:
            self.buyer = buyer
            self.seller = seller
            self.price = price
            return "Contract initiated!"
        return "Contract is already in place."

    def pay(self, buyer, amount):
        # Handles the payment process from the buyer
        # Verifies correct buyer and amount, and updates payment status
        if buyer == self.buyer and amount == self.price and not self.buyer_paid:
            self.buyer_paid = True
            return "Payment received."
        return "Payment failed."

    def deliver_item(self):
        # Manages the item delivery process
        # Checks if payment was made before allowing delivery
        if self.buyer_paid:
            self.item_delivered = True
            return "Item delivered."
        return "Payment not received. Cannot deliver item."

    def finalize_transaction(self):
        # Finalizes the transaction
        # Ensures both payment and delivery are complete
        if self.buyer_paid and self.item_delivered:
            # In a real scenario, this would handle the transfer of funds to the seller
            return f"Transaction finalized. {self.price} transferred to {self.seller}."
        return "Transaction cannot be finalized yet."

    def contract_status(self):
        # Provides the current status of the contract
        return {
            "buyer": self.buyer,
            "seller": self.seller,
            "price": self.price,
            "buyer_paid": self.buyer_paid,
            "item_delivered": self.item_delivered
        }

# Example usage of the SmartContract class
contract = SmartContract()
print(contract.initiate_contract("Alice", "Bob", 100))
print(contract.pay("Alice", 100))
print(contract.deliver_item())
print(contract.finalize_transaction())
