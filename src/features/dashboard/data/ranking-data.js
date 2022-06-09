export const rankingChartData = {
    type: "line",
    data: {
      labels: ["January", "February", "March", "April", "May", "June", "July", "August","September","October","November","December"],
      datasets: [
        {
          label: "Number of Meetings Attended",
          data: [10, 20, 41, 52, 17, 5, 88, 20,60,10,90,32],
          backgroundColor: "rgba(54,73,93,.5)",
          borderColor: "#36495d",
          borderWidth: 3
        },
        {
          label: "Ranking",
          data: [78, 122, 86, 60, 43, 52, 31, 35,24,27,14,8],
          backgroundColor: "rgba(71, 183,132,.5)",
          borderColor: "#47b784",
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      lineTension: 1,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
              padding: 25
            }
          }
        ]
      }
    }
  };
  
  export default rankingChartData;