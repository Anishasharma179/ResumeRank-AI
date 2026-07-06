function UploadJob({
  setJobFile,
  rankCandidates,
  loadingRanking,
}) {
  return (
    <div className="card">

      <h2>💼 Upload Job Description</h2>

      <p>Select the Job Description PDF or DOCX.</p>

      <input
        type="file"
        accept=".pdf,.docx"
        onChange={(e) => setJobFile(e.target.files[0])}
      />

      <button
  onClick={rankCandidates}
  disabled={loadingRanking}
>
  {loadingRanking ? "⏳ Ranking..." : "🏆 Rank Candidates"}
</button>

    </div>
  );
}

export default UploadJob;