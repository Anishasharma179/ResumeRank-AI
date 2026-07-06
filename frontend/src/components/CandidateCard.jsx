function CandidateCard({ candidate }) {

  return (

    <div className="card">

      <h2>Candidate Details</h2>

      {!candidate ? (

        <p>📄 Upload a resume to view candidate details.</p>

      ) : (

        <>
        
          <div
  style={{
    width: 70,
    height: 70,
    borderRadius: "50%",
    background: "#2563eb",
    color: "white",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: "30px",
    marginBottom: "20px",
  }}
>
  👤
</div>
          <p>
            <strong>Name:</strong> {candidate.name}
          </p>

          <p>
            <strong>Email:</strong> {candidate.email}
          </p>

          <p>
            <strong>Phone:</strong> {candidate.phone}
          </p>
          <hr style={{ margin: "20px 0" }} />

          <h4>Skills</h4>

          <div
  style={{
    display: "flex",
    flexWrap: "wrap",
    gap: "10px",
    marginTop: "15px",
  }}
>
  {candidate.skills.map((skill, index) => (
    <span
      key={index}
      style={{
        background: "#2563eb",
        color: "white",
        padding: "8px 14px",
        borderRadius: "20px",
      }}
    >
      {skill}
    </span>
  ))}
</div>

        </>

      )}

    </div>

  );

}

export default CandidateCard;