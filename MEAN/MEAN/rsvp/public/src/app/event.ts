export class Event {
   constructor(
      public event_name: String = "",
      public event_date: Date,
      public rsvp_due_date: Date,
      public guest_list= [],
   ) {}
}
