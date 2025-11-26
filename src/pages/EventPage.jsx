import React from "react";
import { useParams } from "react-router-dom";

const EventPage = () => {
  // get the slug as param
  const { slug } = useParams();

  return <div>EventPage for {slug}</div>;
};

export default EventPage;
