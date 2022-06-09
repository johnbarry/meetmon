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
          voteCount: 113,
          score: 95.5
        },
        {
          rank: 2,
          name: 'Marco Botton',
          email: 'marco.botton@company.com',
          voteCount: 234,
          score: 94.3
        },
        {
          rank: 3,
          name: 'Mariah Macichian',
          email: 'mariah.macichian@company.com',
          voteCount: 164,
          score: 93.1
        },
        {
          rank: 4,
          name: 'Valerie Liberty',
          email: 'valerie.liberty@company.com',
          voteCount: 243,
          score: 92.0
        },
        {
          rank: 5,
          name: 'Christian Halo',
          email: 'christian.halo@company.com',
          voteCount: 243,
          score: 91.4
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
          voteCount: 134,
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
    <div class="filter">
      <div>
        <label>Start date: </label>
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
          <th>Votes</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in ranks" :key="item.email" :class="{ active: item.email === user }">
          <td>{{ item.rank }}</td>
          <td>
            {{ item.name }}
            <span v-if="item.rank === 1">🥇</span>
            <span v-if="item.rank === 2">🥈</span>
            <span v-if="item.rank === 3">🥉</span>
          </td>
          <td class="cell-score">{{ item.score }}</td>
          <td>{{ item.voteCount }}</td>
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

.cell-score {
  text-align: right;
}

td {
  padding: 0.25rem;
}

tr.active td {
  background: lightblue;
}
</style>