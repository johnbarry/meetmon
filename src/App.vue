<script>
export default {
  methods: {
    maybeHighlight: function (item, style) {
      if (item.active) style["background-color"] = "yellow";
      return style;
    },
    setActive: function (number) {
      for (const item of this.agendaItems) {
        item.active = item.number == number;
      }
    },
    updateItemScore: function(item, score) {
      item.scoreCount++
      item.scoreTotal += score
    },
    averageScoreSize: function (avg) {
      if (avg > 3) return 'L'
      if (avg >= 1.5) return 'M'
      if (avg >= 1) return 'S'
      return '0'
    },
    averageItemScore: function (item) {
      return this.averageScoreSize(item.scoreTotal / item.scoreCount)
    },
    sizeToColorMap: function() {
      return {
        L: 'green',
        M: 'lightgreen',
        S: 'orange',
        '0': 'red',
        '': 'lightgrey'
      }
    },
    itemScoreStyle: function (item) {
      return  `background-color: ${  this.sizeToColorMap()[this.averageItemScore(item)] }`
    },
    averageMeetingColor: function (agendaItems) {
      let [totalItems, totalMinutes, totalWeightedScore] = agendaItems.reduce(
        (totals, item) => (!item.minutes || item.scoreCount == 0) ? totals : [ 
          totals[0]+1, // number of items
          totals[1] += item.minutes, // total minutes
          totals[2] += (item.scoreTotal * item.minutes) / item.scoreCount
          ]  ,
        [0, 0, 0.0])
        console.log(`[totalItems, totalMinutes, totalWeightedScore]=[${totalItems} ${totalMinutes} ${totalWeightedScore}]`)
        let color = this.sizeToColorMap()[totalItems == 0 ? '' : this.averageScoreSize(  totalWeightedScore / totalMinutes)]
        console.log(`color is ${color}`)
        return color
    },
  },
  data() {
    function* items(topics, level = 1, number = "") {
      for (const [idx, t] of topics.entries()) {
        let newNumber = number ? `${number}.${idx + 1}` : `${idx + 1}`;
        if (t.name)
          yield {
            number: newNumber,
            title: t.name,
            level: level,
            display: `${"  ".repeat(level - 1)}${t.name}`,
            active: t.active,
            minutes: t.minutes,
            scoreCount: 0,
            scoreTotal: 0
          };

        if (t.topics) yield* items(t.topics, level + 1, newNumber);
      }
    }
    let raw = {
      meetings: {
        1: {
          id: 1,
          time: new Date(),
          title: "Weekly team meeting",
          topics: [
            {
              name: "Recap from last week",
              topics: [
                {
                  ref: "jira-01",
                  name: "Subject A",
                  topics: [
                    {
                      name: "XXX",
                    },
                    {
                      name: "YYY",
                    },
                  ],
                },
                {
                  ref: "jira-02",
                  name: "Subject B",
                },
              ],
              minutes: 10,
            },
            {
              name: "Agree approach for XYZ",
              minutes: 20,
              active: true,
              topics: [
                {
                  name: "AAA",
                },
                {
                  name: "BBB",
                },
              ],
            },
          ],
        },
      },
    };
    raw.agendaItems = Array.from(items(raw.meetings[1].topics));
    return raw;
  },
};
</script>

<template>
  
  <h1>{{ meetings[1].title }} ({{ meetings[1].time.toLocaleString() }}) 
  <button v-bind:style="`background-color: ${averageMeetingColor(agendaItems)}`">score</button>
      
  </h1>
  <table>
    <tbody>
      <tr v-for="item in agendaItems" :key="item.number" :ref="`agenda:${item.number}`">
        <td
          v-bind:style="
            maybeHighlight(item, {
              'background-color': 'lightgrey',
              'font-size': 'small',
            })
          "
          @click="setActive(item.number)"
        > {{ item.number }}
        </td>
        <td 
          v-if="item.level == 1" 
          v-bind:style="maybeHighlight(item, {})"
          @click="setActive(item.number)"
        > {{ item.minutes}} mins
        </td>
        <td 
          v-else
          v-bind:style="maybeHighlight(item, {})"
          @click="setActive(item.number)"
        />
        <td
          v-bind:style="
            maybeHighlight(
              item,
              item.level == 1 ? { 'text-decoration': 'underline' } : {}
            )
          "
          @click="setActive(item.number)"
        >
          {{ item.display }}
        </td>
        <td v-if="item.level == 1"
         @click="updateItemScore(item,0)"
        >
          <button style="background-color: red">0</button>
        </td>
        <td 
          v-if="item.level == 1"
         @click="updateItemScore(item,1)"
          >
          <button style="background-color: orange">S</button>
        </td>
        <td 
          v-if="item.level == 1"
         @click="updateItemScore(item,2)"
          >
          <button style="background-color: lightgreen">M</button>
        </td>
        <td 
          v-if="item.level == 1"
         @click="updateItemScore(item,4)"
          >
          <button style="background-color: green">L</button>
        </td>
        <td v-if="item.level == 1 && item.scoreCount > 0">
        <span style="font-size: small"> x{{item.scoreCount}}
        </span> = 
          <button v-bind:style="itemScoreStyle(item)">
            {{ averageItemScore(item) }}
           </button> 
           
        </td>
      </tr>
    </tbody>
  </table>
</template>

<style>
h1 {
  color: blue;
  font-family: "Courier New", Courier, monospace;
  font-size: large;
}
td {
  color: black;
  font-family: "Courier New", Courier, monospace;
  font-size: normal;
  white-space: pre;
  text-align: left;
  border-spacing: 100px;
}
button {
  color: black;
  font-family: "Courier New", Courier, monospace;
  font-size: small;
  white-space: pre;
  text-align: left;
  border-radius: 50%;
}
</style>
