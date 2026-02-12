import { useEffect, useState } from "react";
import { fetchPrices, fetchChangePoint, fetchEvents } from "./api/api";
import PriceChart from "./components/PriceChart";
import ChangePointCard from "./components/ChangePointCard";
import EventsList from "./components/EventsList";

function App() {
  const [prices, setPrices] = useState([]);
  const [changePoint, setChangePoint] = useState(null);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    const priceRes = await fetchPrices();
    const cpRes = await fetchChangePoint();
    const eventRes = await fetchEvents();

    setPrices(priceRes.data);
    setChangePoint(cpRes.data);
    setEvents(eventRes.data);
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Brent Oil Bayesian Change Point Dashboard</h1>

      <ChangePointCard data={changePoint} />

      <PriceChart
        data={prices}
        changePoint={changePoint?.change_point_date}
      />

      <EventsList events={events} />
    </div>
  );
}

export default App;
