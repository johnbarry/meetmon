<template>
  <div>
    <canvas id="ranking-chart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import rankingChartData from '../ranking-data.js'

export default {
  name: 'RankingChart',
  data() {
    return {
      rankingChartData: rankingChartData
    }
  },
  mounted() {
    const ctx = document.getElementById('ranking-chart');
    new Chart(ctx, this.rankingChartData);
  }
}
</script>