import React from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
} from "chart.js";

ChartJS.register(
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
);

const SalarioGrafico = () => {

  const data = {
    labels: ["Junior", "Pleno", "Sênior"],
    datasets: [
      {
        label: "Salário médio (R$)",
        data: [1800, 4500, 11000], // dados fake por enquanto
        backgroundColor: [
        "#5ed662",
        "#3aa6ff",
        "#c631e0"
      ]
      }
    ]
  };

  return <Bar data={data} />;

};

export default SalarioGrafico;