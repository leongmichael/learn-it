import React, { useState, useRef } from 'react';
import { 
  Play, 
  Pause, 
  Volume2, 
  VolumeX,
  Maximize, 
  Minimize 
} from 'lucide-react';

const VideoPlayer = ({ videoSrc }) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [isMuted, setIsMuted] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  
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

  const handleSeek = (e) => {
    const time = e.target.value;
    if (videoRef.current) {
      videoRef.current.currentTime = time;
      setCurrentTime(time);
    }
  };

  const formatTime = (time) => {
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  return (
    <div className="relative flex flex-col w-full h-full" ref={containerRef}>
      <video
        ref={videoRef}
        className="w-full h-full object-contain"
        src={videoSrc}
        onTimeUpdate={handleTimeUpdate}
        onLoadedMetadata={handleLoadedMetadata}
      />
      
      <div className="absolute bottom-0 left-0 right-0 z-10">
        <div className="bg-black/50 p-4">
          <input
            type="range"
            min="0"
            max={duration}
            value={currentTime}
            onChange={handleSeek}
            className="w-full h-1 mb-4 accent-blue-500 cursor-pointer"
          />
          
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <button 
                onClick={togglePlay} 
                className="text-white hover:text-gray-300 focus:outline-none"
                type="button"
              >
                {isPlaying ? <Pause size={20} /> : <Play size={20} />}
              </button>
              
              <button 
                onClick={toggleMute} 
                className="text-white hover:text-gray-300 focus:outline-none"
                type="button"
              >
                {isMuted ? <VolumeX size={20} /> : <Volume2 size={20} />}
              </button>
              
              <span className="text-white text-sm">
                {formatTime(currentTime)} / {formatTime(duration)}
              </span>
            </div>
            
            <button 
              onClick={toggleFullscreen} 
              className="text-white hover:text-gray-300 focus:outline-none"
              type="button"
            >
              {isFullscreen ? <Minimize size={20} /> : <Maximize size={20} />}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default VideoPlayer;