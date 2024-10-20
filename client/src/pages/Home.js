import {
  Box,
  Typography,
  useTheme,
  useMediaQuery,
  TextField,
  IconButton,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import React, { useState, useEffect, useRef } from "react";
import { ArrowUp } from "lucide-react";
import VideoPlayer from "../components/VideoPlayer.js";
import videoSource from '../components/videos/output_video.mp4';

export default function Home() {
  let navigate = useNavigate();
  const theme = useTheme();
  const [prompt, setPrompt] = useState("");

  const handlePromptChange = (event) => {
    setPrompt(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const apiUrl = `http://127.0.0.1:8000/prompt/${encodeURIComponent(prompt)}`;

    try {
      const response = await fetch(apiUrl, {
        method: "GET",
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error("There has been a problem with your fetch operation:", error);
    }
  };

  return (
    <Box
      sx={{
        minHeight: "100vh",
        width: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        backgroundColor: "#fff",
        padding: { xs: "2rem 1rem", md: "4rem 2rem" },
        gap: "2rem",
      }}
    >
      {/* Header Section */}
      <Box
        sx={{
          textAlign: "center",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          width: "100%",
          maxWidth: "600px",
          mb: 4,
        }}
      >
        <Typography
          variant="h2"
          sx={{
            fontSize: { xs: "56px", sm: "72px" },
            fontWeight: 700,
            color: "#7235FF",
            mb: 1,
            letterSpacing: "-0.02em",
            width: "100%",
          }}
        >
          LearnIt
        </Typography>
        <Typography
          variant="h5"
          sx={{
            fontSize: "24px",
            fontWeight: 400,
            color: "#000",
            width: "100%",
            mb: 4,
          }}
        >
          Learn through generative AI video content.
        </Typography>

        {/* Search Input Section */}
        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            width: "100%",
            gap: 1,
            mb: 4,
          }}
        >
          <TextField
            fullWidth
            placeholder="What do you want to learn about?"
            variant="outlined"
            onChange={handlePromptChange}
            sx={{
              "& .MuiOutlinedInput-root": {
                borderRadius: "50px",
                backgroundColor: "#fff",
                "& fieldset": {
                  borderColor: "#e0e0e0",
                },
                "&:hover fieldset": {
                  borderColor: "#4267B2",
                },
              },
            }}
          />
          <IconButton
            sx={{
              backgroundColor: "#7235FF",
              borderRadius: "50%",
              width: "56px",
              height: "56px",
              "&:hover": {
                backgroundColor: "#5225BC",
              },
            }}
            onClick={handleSubmit}
          >
            <ArrowUp color="white" size={24} />
          </IconButton>
        </Box>
      </Box>

      {/* Video Player Section */}
      <Box
        sx={{
          width: "100%",
          maxWidth: "800px",
          borderRadius: "16px",
          overflow: "hidden",
          boxShadow: "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)",
          backgroundColor: "#000",
          margin: "0 auto",
        }}
      >
        <VideoPlayer videoSrc={videoSource} />
      </Box>
    </Box>
  );
}