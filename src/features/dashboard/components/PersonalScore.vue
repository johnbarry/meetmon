<script>
export default {
  data() {
    return {
      user: 'john.doe@company.com',
      search: '',
      ranks: [
        {
          rank: 1,
          name: 'Giacomo Guilizzoni',
          email: 'giacomo.guilizzoni@company.com',
          voteCount: 113,
          score: 95.5
        }
      ]
    }
  }
}
</script>

<template>
  <h2>Your Score</h2>
  <div class="container">
    <div>
      <div class="score-circle">
        55.6<span>Rank: 421</span>
      </div>
    </div>
    <div class="tips">
      5 Tips for more Effective Meetings:
      <ul>
        <li><a href="#">Decide if you really need the meeting</a></li>
        <li><a href="#">Decide about the audience</a></li>
        <li><a href="#">Plan and structure meetings</a></li>
        <li><a href="#">Keep meetings on track</a></li>
        <li><a href="#">Sum up and Finish on time</a></li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  margin-bottom: 2rem;
}
.score-circle {
  margin-left: 2rem;
  font-size: 2rem;
  border-radius: 50%;
  background-color: orange;
  padding: 3rem;
  width: fit-content;
  text-align: center;
}
.score-circle > span {
  display: block;
  font-size: 1rem;
}
.tips {
  margin-left: 6rem;
}
</style>