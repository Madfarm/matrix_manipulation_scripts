function createAccount(pin, amount = 0) {
    let balance = amount;
    let currentPin = pin;
  
    return {
      checkBalance: function(pin) {
        if (pin !== currentPin) {
          console.error("Invalid PIN");
          return;
        }
        console.log(`Current balance: $${balance}`);
      },
      deposit: function(pin, amount) {
        if (pin !== currentPin) {
          console.error("Invalid PIN");
          return;
        }
        balance += amount;
        console.log(`Deposit successful. New balance: $${balance}`);
      },
      withdraw: function(pin, amount) {
        if (pin !== currentPin) {
          console.error("Invalid PIN");
          return;
        }
        if (amount > balance) {
          console.error("Insufficient funds");
          return;
        }
        balance -= amount;
        console.log(`Withdrawal successful. New balance: $${balance}`);
      },
      changePin: function(oldPin, newPin) {
        if (oldPin !== currentPin) {
          console.error("Invalid PIN");
          return;
        }
        currentPin = newPin;
        console.log("PIN changed successfully");
      }
    };
  }


const account = createAccount(1234, 1000);
account.checkBalance(1234); // outputs "Current balance: $1000"
account.deposit(1234, 500); // outputs "Deposit successful. New balance: $1500"
account.withdraw(1234, 200); // outputs "Withdrawal successful. New balance: $1300"
account.changePin(1234, 5678); // outputs "PIN changed successfully"
account.checkBalance(5678); // outputs "Current balance: $1300"
                  