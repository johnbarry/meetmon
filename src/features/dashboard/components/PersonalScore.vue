<script>
export default {
  data() {
    return {
      score: 55.6,
      rank: 521
    }
  }
}
</script>

<template>
  <h2>Your Score</h2>
  <div class="container">
    <div>
      <div class="score-circle">
        {{score}}/100<span>Rank: {{rank}}</span>
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
  margin-bottom: 3rem;
}
.score-circle {
  margin-left: 2rem;
  font-size: 2rem;
  border-radius: 50%;
  background-color: orange;
  padding: 3.5rem 2rem;
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