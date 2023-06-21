import React from "react";
import { ReactMediaRecorder } from "react-media-recorder";
import RecorderIcon from "./RecorderIcon.tsx";

interface Props {
  handleStop: any;
}

const RecordMessage = ({ handleStop }: Props) => {
  return (
    <ReactMediaRecorder
      audio
      onStop={handleStop}
      render={({ status, startRecording, stopRecording }) => (
        <div className="mt-2">
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className="bg-white p-4 rounded-full"
          >
            <RecorderIcon classText={ status === "recording" ? "animate-pulse text-red-500 " : " text-sky-500"} />
          </button>
          <p className="mt-2 text-white font-light">{status}</p>
        </div>
      )}
    />
  );
};

export default RecordMessage;
