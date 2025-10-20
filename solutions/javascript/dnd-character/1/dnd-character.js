//
// This is only a SKELETON file for the 'D&D Character' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const abilityModifier = (stat) => {
  if (stat < 3) throw new Error("Ability scores must be at least 3");
  if (stat > 18) throw new Error("Ability scores can be at most 18");
  return Math.floor((stat - 10) / 2);
};

export class Character {
  constructor() {
    this.str = Character.rollAbility();
    this.dex = Character.rollAbility();
    this.con = Character.rollAbility();
    this.int = Character.rollAbility();
    this.wis = Character.rollAbility();
    this.cha = Character.rollAbility();
    this.hp = 10 + abilityModifier(this.con);
  }

  static rollAbility() {
    const rolls = [...Array(4)].map(() => Math.floor(Math.random() * 6) + 1);
    rolls.sort((a, b) => a - b);
    return rolls.slice(1).reduce((a, b) => a + b);
  }

  get strength() {
    return this.str;
  }

  get dexterity() {
    return this.dex;
  }

  get constitution() {
    return this.con;
  }

  get intelligence() {
    return this.int;
  }

  get wisdom() {
    return this.wis;
  }

  get charisma() {
    return this.cha;
  }

  get hitpoints() {
    return this.hp;
  }
}
