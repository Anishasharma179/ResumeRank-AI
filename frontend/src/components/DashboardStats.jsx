function DashboardStats({ rankings }) {
  const totalCandidates = rankings.length;

  const highestScore =
    rankings.length > 0
      ? Math.max(...rankings.map((c) => c.score))
      : 0;

  const averageScore =
    rankings.length > 0
      ? (
          rankings.reduce((sum, c) => sum + c.score, 0) /
          rankings.length
        ).toFixed(1)
      : 0;

  const cards = [
    {
      title: "Candidates",
      value: totalCandidates,
      color: "#2563eb",
    },
    {
      title: "Average Score",
      value: averageScore + "%",
      color: "#10b981",
    },
    {
      title: "Highest Score",
      value: highestScore + "%",
      color: "#f59e0b",
    },
  ];

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
        gap: "20px",
        marginBottom: "30px",
      }}
    >
      {cards.map((card) => (
        <div
          key={card.title}
          className="card"
          style={{
            borderLeft: `6px solid ${card.color}`,
          }}
        >
          <h3>{card.title}</h3>

          <h1
            style={{
              color: card.color,
              margin: "10px 0",
            }}
          >
            {card.value}
          </h1>
        </div>
      ))}
    </div>
  );
}

export default DashboardStats;