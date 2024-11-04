import {
  Box,
  Typography,
  TextField,
  IconButton,
  CircularProgress,
  Snackbar,
  Alert,
  LinearProgress,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import React, { useState } from "react";
import { ArrowUp } from "lucide-react";
import VideoPlayer from "../components/VideoPlayer.js";
import videoSource from "../components/videos/output_video.mp4";
const electron = window.require('electron');
const { ipcRenderer } = electron;

export default function Home() {
  let navigate = useNavigate();
  const [prompt, setPrompt] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [snackbar, setSnackbar] = useState({
    open: false,
    message: "",
    severity: "success"
  });

  const handlePromptChange = (event) => {
    setPrompt(event.target.value);
  };

  const handleCloseSnackbar = () => {
    setSnackbar(prev => ({ ...prev, open: false }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    if (!prompt.trim()) {
      setSnackbar({
        open: true,
        message: "Please enter a prompt first",
        severity: "warning"
      });
      return;
    }
    
    if (!ipcRenderer) {
      setSnackbar({
        open: true,
        message: "System error: ipcRenderer not available",
        severity: "error"
      });
      return;
    }
    
    try {
      setIsLoading(true);
      console.log("Attempting to invoke run-python");
      const result = await ipcRenderer.invoke('run-python', prompt);
      console.log('Python process completed with code:', result);
      
      if (result === 0) {
        setSnackbar({
          open: true,
          message: "Video generated successfully!",
          severity: "success"
        });
      } else {
        setSnackbar({
          open: true,
          message: "Error generating video",
          severity: "error"
        });
      }
    } catch (error) {
      console.error("Error running Python script:", error);
      setSnackbar({
        open: true,
        message: `Error: ${error.message || "Failed to generate video"}`,
        severity: "error"
      });
    } finally {
      setIsLoading(false);
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
            value={prompt}
            onChange={handlePromptChange}
            disabled={isLoading}
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
              "&.Mui-disabled": {
                backgroundColor: "#9B7ECC",
              },
            }}
            onClick={handleSubmit}
            disabled={isLoading}
          >
            {isLoading ? (
              <CircularProgress size={24} color="inherit" sx={{ color: "white" }} />
            ) : (
              <ArrowUp color="white" size={24} />
            )}
          </IconButton>
        </Box>
      </Box>

      {isLoading && (
        <Box sx={{ width: '100%', maxWidth: '600px', mb: 2 }}>
          <Typography variant="body2" color="text.secondary" align="center" sx={{ mb: 1 }}>
            Generating your video... This may take a few minutes
          </Typography>
          <LinearProgress sx={{ 
            height: 8,
            borderRadius: 4,
            backgroundColor: '#E0E0E0',
            '& .MuiLinearProgress-bar': {
              backgroundColor: '#7235FF',
            }
          }} />
        </Box>
      )}

      <Box
        sx={{
          width: "100%",
          maxWidth: "800px",
          borderRadius: "16px",
          overflow: "hidden",
          boxShadow:
            "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)",
          backgroundColor: "#000",
          margin: "0 auto",
          marginTop: -8,
        }}
      >
        <VideoPlayer videoSrc={videoSource} />
      </Box>

      <Snackbar 
        open={snackbar.open} 
        autoHideDuration={6000} 
        onClose={handleCloseSnackbar}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert 
          onClose={handleCloseSnackbar} 
          severity={snackbar.severity}
          variant="filled"
          sx={{ width: '100%' }}
        >
          {snackbar.message}
        </Alert>
      </Snackbar>
    </Box>
  );
}
