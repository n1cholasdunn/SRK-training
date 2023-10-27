export type Day = { day: string; slots: Slot[]; comment: string };

export type Slot = { from: string; to: string };

export type Availability = { [key: string]: Day };
