<script>
import LeaderboardTable from './features/dashboard/components/LeaderboardTable.vue';

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
    updateItemScore: function (item, score) {
      item.scoreCount++;
      item.scoreTotal += score;
    },
    averageScoreSize: function (avg) {
      if (avg > 3) return "L";
      if (avg >= 1.5) return "M";
      if (avg >= 1) return "S";
      return "0";
    },
    averageItemScore: function (item) {
      return this.averageScoreSize(item.scoreTotal / item.scoreCount);
    },
    sizeToColorMap: function () {
      return {
        L: "green",
        M: "lightgreen",
        S: "orange",
        0: "red",
        "": "lightgrey",
      };
    },
    itemScoreStyle: function (item) {
      return `background-color: ${this.sizeToColorMap()[this.averageItemScore(item)]}`;
    },
    averageMeetingColor: function (agendaItems) {
      let [totalItems, totalMinutes, totalWeightedScore] = agendaItems.reduce(
        (totals, item) =>
          !item.minutes || item.scoreCount == 0
            ? totals
            : [
              totals[0] + 1, // number of items
              (totals[1] += item.minutes), // total minutes
              (totals[2] += (item.scoreTotal * item.minutes) / item.scoreCount),
            ],
        [0, 0, 0.0]
      );
      console.log(
        `[totalItems, totalMinutes, totalWeightedScore]=[${totalItems} ${totalMinutes} ${totalWeightedScore}]`
      );
      let color = this.sizeToColorMap()[
        totalItems == 0 ? "" : this.averageScoreSize(totalWeightedScore / totalMinutes)
      ];
      console.log(`color is ${color}`);
      return color;
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
            active: t.active,
            minutes: t.minutes,
            notes: t.notes,
            scoreCount: 0,
            scoreTotal: 0,
          };

        if (t.topics) yield* items(t.topics, level + 1, newNumber);
      }
    }
    let urlParams = new URLSearchParams(window.location.search);
    let raw = {
      defaultMeeting: urlParams.has("id") ? urlParams.get("id") : 1,
      meetings: {
        2: {
          id: 2,
          time: new Date(),
          title: "Kickoff",
          topics: [
            {
              name: "Change current meeting page - John, Anil, Syed",
              minutes: 5,
              notes: [
                "stepping thru agenda",
                "entering meeting minutes",
                "algo discussion",
              ],
            },
            {
              name: "Design/implmenent ratings page - Daniel, Gaurav, Naveen",
              active: true,
              minutes: 5,
              notes: [
                "focus on UI, wireframes",
                "simple, ordered list",
                "averages not single meeting",
              ],
            },
            {
              name: "Teams integration - Syed, Daniel",
              minutes: 5,
              notes: ["ON HOLD"],
            },
            {
              name: "Objective",
              minutes: 1,
              notes: [
                "Provide chair rating to enable participants to choose effective meetings and a means for chairs to improve",
              ],
            },
          ],
        },
        1: {
          id: 1,
          time: new Date(),
          title: "Weekly team meeting",
          topics: [
            {
              name: "Recap from last week",
              active: true,
              topics: [
                {
                  ref: "jira-01",
                  name: "Sally presented the new features",
                  topics: [
                    {
                      name: "Button color changes",
                      notes: [
                        "Harry said it was super cool",
                        "Nadia wasn't so impressed",
                      ],
                    },
                    {
                      name: "Save button",
                    },
                  ],
                },
                {
                  ref: "jira-02",
                  name: "Agreed to use green over blue for background colors",
                },
              ],
              minutes: 10,
            },
            {
              name: "Agree approach for database migration",
              minutes: 30,
              topics: [
                {
                  name: "Big bang approach: Pros & cons",
                  notes: ["Pro: Simple to implement", "Con: High release failure risk"],
                },
                {
                  name: "Incremental change: Pros & Cons",
                  notes: [
                    "Con: Need feature switch for new/old database approach",
                    "Con: Twice as many test cases",
                    "Pro: Easier to revert",
                    "Pro: Less likely to get fired",
                  ],
                },
                {
                  name: "Propose big bang or incremental",
                  notes: [
                    "Decided on incremental approach",
                    "Joe to produce plan for next week's meeting",
                    "Getting fired is bad",
                  ],
                },
              ],
            },
          ],
        },
      },
    };
    raw.agendaItems = Array.from(items(raw.meetings[raw.defaultMeeting].topics));
  raw.justLevelOne = raw.agendaItems.reduce( (levelOneSoFar, item) => levelOneSoFar && item.level == 1 )
    return raw;
  },
  components: {
    LeaderboardTable
  }
};
</script>

<template>
  <LeaderboardTable></LeaderboardTable>
<!-- <h1>
    {{ meetings[1].title }} ({{ meetings[1].time.toLocaleString() }})
    <button v-bind:style="`background-color: ${averageMeetingColor(agendaItems)}`">
      score
    </button>
  </h1>
  <table>
    <thead>
      <tr>
        <th>Item</th>
        <th>Time</th>
        <th>Subject</th>
        <th>Minutes</th>
        <th colspan="5">Score</th>
      </tr>
    </thead>
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
        >
          {{ item.number }}
        </td>
        <td
          v-if="item.level == 1"
          v-bind:style="maybeHighlight(item, {})"
          @click="setActive(item.number)"
        >
          {{ item.minutes }} mins
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
              item.level == 1 && !justLevelOne ? { 'text-decoration': 'underline' } : {}
            )
          "
          @click="setActive(item.number)"
        >
          <span v-if="item.level == 1">{{ item.title }}</span>
          <span v-else>{{ `${"  ".repeat(item.level - 2)}- ${item.title}` }}</span>
        </td>

        <td
          v-bind:style="maybeHighlight(item, { 'font-size': 'small' })"
          @click="setActive(item.number)"
        >
          <ol>
            <li v-for="n in item.notes">{{ n }}</li>
          </ol>
        </td>

        <td
          v-if="item.level == 1"
          v-bind:style="maybeHighlight(item, {})"
          @click="updateItemScore(item, 0)"
        >
          <button style="background-color: red">0</button>
        </td>
        <td
          v-if="item.level == 1"
          v-bind:style="maybeHighlight(item, {})"
          @click="updateItemScore(item, 1)"
        >
          <button style="background-color: orange">S</button>
        </td>
        <td
          v-if="item.level == 1"
          v-bind:style="maybeHighlight(item, {})"
          @click="updateItemScore(item, 2)"
        >
          <button style="background-color: lightgreen">M</button>
        </td>
        <td
          v-if="item.level == 1"
          v-bind:style="maybeHighlight(item, {})"
          @click="updateItemScore(item, 4)"
        >
          <button style="background-color: green">L</button>
        </td>
        <td
          v-if="item.level == 1 && item.scoreCount > 0"
          v-bind:style="maybeHighlight(item, {})"
        >
          <span style="font-size: small"> x{{ item.scoreCount }} </span> =
          <button v-bind:style="itemScoreStyle(item)">
            {{ averageItemScore(item) }}
          </button>
        </td>
      </tr>
    </tbody>
  </table>-->
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
th {
  color: black;
  font-family: "Courier New", Courier, monospace;
  font-size: normal;
  border-spacing: 100px;
  background-color: lightgrey;
  text-decoration: underline;
}
button {
  color: black;
  font-family: "Courier New", Courier, monospace;
  font-size: small;
  white-space: pre;
  text-align: left;
  border-radius: 50%;
}
ol {
  margin-top: 0;
  margin-bottom: 0;
  color: blue;
}
</style>
