import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    ResponsiveContainer,
    ReferenceLine
  } from "recharts";
  
  export default function PriceChart({ data, changePoint }) {
    return (
      <div style={{ width: "100%", height: 500 }}>
        <ResponsiveContainer>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="Date" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="Price" stroke="#2563eb" dot={false} />
  
            {changePoint && (
              <ReferenceLine
                x={changePoint}
                stroke="red"
                label="Change Point"
              />
            )}
          </LineChart>
        </ResponsiveContainer>
      </div>
    );
  }
  