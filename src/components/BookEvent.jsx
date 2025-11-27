import { useState, useRef } from "react";
import emailjs from "@emailjs/browser";

const BookEvent = ({ eventName, eventDetail }) => {
  const form = useRef();
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);

    const SERVICE_ID = "service_eqs914o";
    const TEMPLATE_ID = "template_fpfg7tl";
    const PUBLIC_KEY = "v8pA_DkmPyxjPG5T0";

    emailjs
      .sendForm(SERVICE_ID, TEMPLATE_ID, form.current, {
        publicKey: PUBLIC_KEY,
      })
      .then(
        () => {
          console.log("SUCCESS!");
          setSubmitted(true);
          setLoading(false);
        },
        (error) => {
          console.log("FAILED...", error.text);
          setLoading(false);
          alert("Failed to send email. Please try again.");
        }
      );
  };
  return (
    <div id="book-event">
      {submitted ? (
        <p className="text-sm">ThankYou for signing up!</p>
      ) : (
        <form ref={form} onSubmit={handleSubmit}>
          <input type="hidden" name="event_name" value={eventName} />
          <input type="hidden" name="message" value={eventDetail} />
          <input
            type="hidden"
            name="subject"
            value={`Booking for ${eventName}`}
          />

          <div>
            <label htmlFor="name">Name</label>
            <input
              type="text"
              name="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              id="name"
              placeholder="Enter your name"
              required
            />
          </div>

          <div>
            <label htmlFor="email">Email Address</label>
            <input
              type="email"
              name="user_email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              id="email"
              placeholder="Enter your email address"
            />
          </div>

          <button type="submit" disabled={loading} className="button-submit">
            {loading ? "Sending..." : "Submit"}
          </button>
        </form>
      )}
    </div>
  );
};

export default BookEvent;
