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

const SalarioGrafico = ({ dados }) => {

  if (!dados) return null;

  const data = {
    labels: ["Júnior", "Pleno", "Sênior", "Média"], 
    datasets: [
      {
        label: "Salário médio (R$)",
        data: [
          dados.salario_junior,
          dados.salario_pleno,
          dados.salario_senior,
          dados.media 
        ],
        backgroundColor: [
          "#a53434",
          "#c02ba7",
          "#22b8a4",
          "#8d2eaa" 
        ],
        borderRadius: 8
      }
    ]
  };

  const options = {
    plugins: {
      legend: {
        labels: {
          font: {
            size: 18
          }
        }
      }
    },
    scales: {
      x: {
        ticks: {
          font: {
            size: 18
          }
        }
      },
      y: {
        ticks: {
          font: {
            size: 18
          }
        }
      }
    }
  };

  return <Bar data={data} options={options} />;
};

export default SalarioGrafico;