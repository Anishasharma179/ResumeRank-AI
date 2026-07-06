function RankingTable({ rankings }) {
  function getMedal(index) {
    if (index === 0) return "🥇";
    if (index === 1) return "🥈";
    if (index === 2) return "🥉";
    return "🏅";
  }

  function getScoreColor(score) {
    if (score >= 80) return "#10b981";
    if (score >= 60) return "#f59e0b";
    return "#ef4444";
  }

  return (
    <div className="card">

      <h2>🏆 Candidate Rankings</h2>

      {rankings.length === 0 ? (

        <p>📊 No ranking available. Upload a Job Description to generate rankings.</p>
      ) : (

        <table>

          <thead>

            <tr>
              <th>Rank</th>
              <th>Name</th>
              <th>Email</th>
              <th>Score</th>
              <th>Matched Skills</th>
              <th>Missing Skills</th>
            </tr>

          </thead>

          <tbody>

            {rankings.map((candidate, index) => (

              <tr key={candidate.id}>

                <td
                  style={{
                    fontSize: "22px",
                    textAlign: "center",
                  }}
                >
                  {getMedal(index)}
                </td>

                <td>{candidate.name}</td>

                <td>{candidate.email}</td>

                <td>

                  <div
                    style={{
                      background: "#e5e7eb",
                      borderRadius: "20px",
                      overflow: "hidden",
                    }}
                  >

                    <div
                      style={{
                        width: `${candidate.score}%`,
                        background: getScoreColor(candidate.score),
                        transition: "width .8s ease",
                        color: "white",
                        textAlign: "center",
                        padding: "5px",
                        fontWeight: "bold",
                      }}
                    >
                      {candidate.score}%
                    </div>

                  </div>

                </td>

                <td>

                  {candidate.matched_skills.map((skill) => (

                    <span
                      key={skill}
                      style={{
                        background: "#dcfce7",
                        color: "#166534",
                        padding: "5px 10px",
                        margin: "3px",
                        borderRadius: "20px",
                        display: "inline-block",
                      }}
                    >
                      {skill}
                    </span>

                  ))}

                </td>

                <td>

                  {candidate.missing_skills.map((skill) => (

                    <span
                      key={skill}
                      style={{
                        background: "#fee2e2",
                        color: "#991b1b",
                        padding: "5px 10px",
                        margin: "3px",
                        borderRadius: "20px",
                        display: "inline-block",
                      }}
                    >
                      {skill}
                    </span>

                  ))}

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      )}

    </div>
  );
}

export default RankingTable;