//
// This is only a SKELETON file for the 'Bank Account' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export class BankAccount {
  constructor() {
    this.status = false;
    this.saldo = 0;
  }

  open() {
    if (!this.status) this.status = true;
    else throw new ValueError();
  }

  close() {
    if (this.status) {
      this.status = false;
      this.saldo = 0;
    } else throw new ValueError();
  }

  deposit(money) {
    if (this.status && money > 0) this.saldo += money;
    else throw new ValueError();
  }

  withdraw(money) {
    if (this.status && money > 0 && money <= this.saldo) this.saldo -= money;
    else throw new ValueError();
  }

  get balance() {
    if (this.status) return this.saldo;
    else throw new ValueError();
  }
}

export class ValueError extends Error {
  constructor() {
    super("Bank account error");
  }
}
