<script>
import Chart from 'chart.js'
import rankingChartData from '../data/ranking-data';

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

<template>
  <h2>Your Rating Trend</h2>
  <div class="container">
    <canvas id="ranking-chart"></canvas>
  </div>
</template>


<style scoped>
.container {
  max-width: 600px;
}
</style>