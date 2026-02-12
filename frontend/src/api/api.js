import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000/api"
});

export const fetchPrices = () => API.get("/prices/");
export const fetchChangePoint = () => API.get("/changepoints/");
export const fetchEvents = () => API.get("/events/");
