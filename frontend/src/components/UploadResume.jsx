function UploadResume({
  setResumeFile,
  uploadResume,
  loadingResume,
}) {
  return (
    <div className="card">

      <h2>📄 Upload Resume</h2>

      <p>Select a PDF or DOCX resume.</p>

      <input
        type="file"
        accept=".pdf,.docx"
        onChange={(e) => setResumeFile(e.target.files[0])}
      />

      <button
  onClick={uploadResume}
  disabled={loadingResume}
>
  {loadingResume ? "⏳ Uploading..." : "📄 Upload Resume"}
</button>

    </div>
  );
}

export default UploadResume;