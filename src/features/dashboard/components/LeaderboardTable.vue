<script>
export default {
  data() {
    return {
      user: 'john.doe@company.com',
      ranks: [
        {
          rank: 1,
          name: 'Giacomo Guilizzoni',
          email: 'giacomo.guilizzoni@company.com',
          score: 95.5
        },
        {
          rank: 2,
          name: 'Marco Botton',
          email: 'marco.botton@company.com',
          score: 94.3
        },
        {
          rank: 3,
          name: 'Mariah Macichian',
          email: 'mariah.macichian@company.com',
          score: 93.1
        },
        {
          rank: 4,
          name: 'Valerie Liberty',
          email: 'valerie.liberty@company.com',
          score: 92.0
        },
        {
          rank: '...',
          name: '...',
          email: '...',
          score: '...'
        },
        {
          rank: 521,
          name: 'John Doe',
          email: 'john.doe@company.com',
          score: 55.6
        }
      ]
    }
  }
}
</script>

<template>
  <div class="container">
    <h1>Leaderboard</h1>
    <p>This shows the meeting organiser leaders.</p>
    <div class="filter">
      <div>
        <label>Start date:</label>
        <input type="date" id="start" value="2022-04-10">
      </div>
      <div>
        <input type="text" placeholder="search people">
      </div>
    </div>
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Name</th>
          <th>Meeting Score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Giacomo Guzioni 👑🏆🥇🥈🥉</td>
          <td>97.5</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  max-width: 600px;
}

.filter {
  display: flex;
  justify-content: right;
  margin-bottom: .5rem;
}

.filter div+div {
  margin-left: .5rem;
}
</style>