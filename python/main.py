# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


meetings= {
        2: {
          id: 2,
          time: new Date("2022-06-09T11:00:00"),
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
      }

@app.get('/meeting/<meetingid>')
def show_user_profile(meetingid):
    return jsonify(meetings[int(meetingid)]), 200

