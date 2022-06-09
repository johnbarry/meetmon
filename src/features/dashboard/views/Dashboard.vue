<script>
import LeaderboardTable from '../components/LeaderboardTable.vue';
import PersonalScore from '../components/PersonalScore.vue';
import RatingChart from '../components/RatingChart.vue';

export default {
  components: {
    LeaderboardTable,
    PersonalScore,
    RatingChart
  }
};
</script>

<template>
  <h1>Meeting Rating</h1>
  <LeaderboardTable></LeaderboardTable>
  <PersonalScore></PersonalScore>
  <RatingChart></RatingChart>
</template>