import React, { useState, useRef } from "react";
import {
  Play,
  Pause,
  Volume2,
  VolumeX,
  Maximize,
  Minimize,
} from "lucide-react";
import {
  Box,
  IconButton,
  Slider,
  Typography,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
} from "@mui/material";

const VideoPlayer = ({ videoSrc }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isMuted, setIsMuted] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [playbackRate, setPlaybackRate] = useState(1);

  const videoRef = useRef(null);
  const containerRef = useRef(null);

  const togglePlay = () => {
    if (videoRef.current) {
      if (isPlaying) {
        videoRef.current.pause();
      } else {
        videoRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const toggleMute = () => {
    if (videoRef.current) {
      videoRef.current.muted = !isMuted;
      setIsMuted(!isMuted);
    }
  };

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      containerRef.current.requestFullscreen();
      setIsFullscreen(true);
    } else {
      document.exitFullscreen();
      setIsFullscreen(false);
    }
  };

  const handleTimeUpdate = () => {
    if (videoRef.current) {
      setCurrentTime(videoRef.current.currentTime);
    }
  };

  const handleLoadedMetadata = () => {
    if (videoRef.current) {
      setDuration(videoRef.current.duration);
    }
  };

  const handleSeek = (e, newValue) => {
    if (videoRef.current) {
      videoRef.current.currentTime = newValue;
      setCurrentTime(newValue);
    }
  };

  const handlePlaybackRateChange = (event) => {
    const rate = event.target.value;
    setPlaybackRate(rate);
    if (videoRef.current) {
      videoRef.current.playbackRate = rate;
    }
  };

  const formatTime = (time) => {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, "0")}`;
  };

  return (
    <Box
      ref={containerRef}
      sx={{ position: "relative", width: "100%", height: "100%" }}
    >
      <video
        ref={videoRef}
        src={videoSrc}
        onTimeUpdate={handleTimeUpdate}
        onLoadedMetadata={handleLoadedMetadata}
        style={{ width: "100%", height: "100%", objectFit: "contain" }}
      />
      <Box
        sx={{
          position: "absolute",
          bottom: 0,
          left: 0,
          right: 0,
          background: "rgba(0, 0, 0, 0.5)",
          padding: "8px 16px",
          display: "flex",
          flexDirection: "column",
          gap: "8px",
        }}
      >
        <Slider
          min={0}
          max={duration}
          value={currentTime}
          onChange={handleSeek}
          sx={{ color: "#7235FF" }}
        />
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <Box sx={{ display: "flex", gap: "8px", alignItems: "center" }}>
            <IconButton onClick={togglePlay} sx={{ color: "#7235FF" }}>
              {isPlaying ? <Pause /> : <Play />}
            </IconButton>
            <IconButton onClick={toggleMute} sx={{ color: "#7235FF" }}>
              {isMuted ? <VolumeX /> : <Volume2 />}
            </IconButton>
            <Typography variant="body2" sx={{ color: "#7235FF" }}>
              {formatTime(currentTime)} / {formatTime(duration)}
            </Typography>
            <FormControl
              variant="standard"
              sx={{ marginLeft: 1, minWidth: 80, color: "#7235FF" }}
            >
              <InputLabel id="playback-rate-label" sx={{ color: "#7235FF" }}>
                Speed
              </InputLabel>
              <Select
                labelId="playback-rate-label"
                id="playback-rate"
                value={playbackRate}
                onChange={handlePlaybackRateChange}
                sx={{
                  color: "#7235FF",
                  "& .MuiSvgIcon-root": { color: "#7235FF" },
                }}
              >
                <MenuItem value={0.5}>0.5x</MenuItem>
                <MenuItem value={0.75}>0.75x</MenuItem>
                <MenuItem value={1}>1x</MenuItem>
                <MenuItem value={1.5}>1.5x</MenuItem>
                <MenuItem value={2}>2x</MenuItem>
              </Select>
            </FormControl>
          </Box>
          <IconButton onClick={toggleFullscreen} sx={{ color: "#7235FF" }}>
            {isFullscreen ? <Minimize /> : <Maximize />}
          </IconButton>
        </Box>
      </Box>
    </Box>
  );
};

export default VideoPlayer;
