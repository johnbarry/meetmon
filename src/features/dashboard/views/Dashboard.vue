<script>
import LeaderboardTable from '../components/LeaderboardTable.vue';
import PersonalScore from '../components/PersonalScore.vue';

export default {
  components: {
    LeaderboardTable,
    PersonalScore
  }
};
</script>

<template>
  <h1>Meeting Rating</h1>
  <LeaderboardTable></LeaderboardTable>
  <PersonalScore></PersonalScore>
</template>

<style scoped>

</style>