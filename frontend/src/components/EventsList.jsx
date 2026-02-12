export default function EventsList({ events }) {
    return (
      <div style={{ marginTop: "30px" }}>
        <h2>Geopolitical Events</h2>
        <ul>
          {events.map((event, index) => (
            <li key={index}>
              <strong>{new Date(event.Date).toLocaleDateString()}:</strong>{" "}
              {event.Event}
            </li>
          ))}
        </ul>
      </div>
    );
  }
  