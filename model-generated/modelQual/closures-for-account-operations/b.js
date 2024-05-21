function createAccount(initialPin, initialAmount = 0) {
    let pin = initialPin;
    let balance = initialAmount;
  
    return {
      // Check balance
      checkBalance(inputPin) {
        if (inputPin === pin) {
          return `Your balance is $${balance}.`;
        } else {
          return "Invalid PIN.";
        }
      },
  
      // Deposit
      deposit(inputPin, amount) {
        if (inputPin === pin) {
          if (amount <= 0) {
            return "Deposit amount must be positive.";
          }
          balance += amount;
          return `Deposited $${amount}. New balance is $${balance}.`;
        } else {
          return "Invalid PIN.";
        }
      },
  
      // Withdraw
      withdraw(inputPin, amount) {
        if (inputPin === pin) {
          if (amount <= 0) {
            return "Withdraw amount must be positive.";
          }
          if (amount > balance) {
            return "Insufficient funds.";
          }
          balance -= amount;
          return `Withdrew $${amount}. New balance is $${balance}.`;
        } else {
          return "Invalid PIN.";
        }
      },
  
      // Change PIN
      changePin(inputPin, newPin) {
        if (inputPin === pin) {
          pin = newPin;
          return "PIN has been successfully changed.";
        } else {
          return "Invalid PIN.";
        }
      }
    };
  }
  
  // Example usage:
  const myAccount = createAccount('1234', 100);
  console.log(myAccount.checkBalance('1234'));   // "Your balance is $100."
  console.log(myAccount.deposit('1234', 50));    // "Deposited $50. New balance is $150."
  console.log(myAccount.withdraw('1234', 75));   // "Withdrew $75. New balance is $75."
  console.log(myAccount.changePin('1234', '5678')); // "PIN has been successfully changed."
  console.log(myAccount.checkBalance('1234'));   // "Invalid PIN."
  console.log(myAccount.checkBalance('5678'));   // "Your balance is $75."