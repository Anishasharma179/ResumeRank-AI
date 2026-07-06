import DashboardStats from "./components/DashboardStats";
import { useState } from "react";
import "./App.css";

import api from "./api/api";

import Header from "./components/Header";
import UploadResume from "./components/UploadResume";
import UploadJob from "./components/UploadJob";
import CandidateCard from "./components/CandidateCard";
import RankingTable from "./components/RankingTable";
import Footer from "./components/Footer";

function App() {
  const [resumeFile, setResumeFile] = useState(null);
  const [jobFile, setJobFile] = useState(null);

  const [candidate, setCandidate] = useState(null);
  const [rankings, setRankings] = useState([]);

  const [loadingResume, setLoadingResume] = useState(false);
  const [loadingRanking, setLoadingRanking] = useState(false);

  async function uploadResume() {
    if (!resumeFile) {
      alert("Please select a resume.");
      return;
    }

    const formData = new FormData();
    formData.append("file", resumeFile);

    try {
      setLoadingResume(true);

      const response = await api.post("/upload", formData);


      setCandidate(response.data.candidate);

    } catch (error) {
      console.error(error);
      alert("Resume upload failed.");
    } finally {
      setLoadingResume(false);
    }
  }

  async function rankCandidates() {
    if (!jobFile) {
      alert("Please select a job description.");
      return;
    }

    const formData = new FormData();
    formData.append("file", jobFile);

    try {
      setLoadingRanking(true);

      const response = await api.post("/job", formData);


      setRankings(response.data.rankings);

    } catch (error) {
      console.error(error);
      alert("Ranking failed.");
    } finally {
      setLoadingRanking(false);
    }
  }

  return (
  <div className="container">

    <Header />

    <DashboardStats
      candidate={candidate}
      rankings={rankings}
    />

    <div className="dashboard-grid">

      <UploadResume
        resumeFile={resumeFile}
        setResumeFile={setResumeFile}
        uploadResume={uploadResume}
        loadingResume={loadingResume}
      />

      <UploadJob
        jobFile={jobFile}
        setJobFile={setJobFile}
        rankCandidates={rankCandidates}
        loadingRanking={loadingRanking}
      />

    </div>

    <CandidateCard candidate={candidate} />

    <RankingTable rankings={rankings} />
    <Footer />

  </div>
);
}

export default App;