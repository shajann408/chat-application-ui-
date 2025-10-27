import React, { useState, useRef, useEffect } from "react";
import { PaperPlane, Smile, Paperclip, X } from "lucide-react";

// Default export: ChatUI component
export default function ChatUI() {
  const [messages, setMessages] = useState([
    { id: 1, from: "them", text: "Hey! Welcome to the chat.", time: "11:00 AM" },
    { id: 2, from: "me", text: "Hi — nice UI!", time: "11:01 AM" },
  ]);
  const [text, setText] = useState("");
  const [showEmoji, setShowEmoji] = useState(false);
  const [attachment, setAttachment] = useState(null);
  const listRef = useRef(null);

  useEffect(() => {
    // auto-scroll to bottom when messages change
    if (listRef.current) {
      listRef.current.scrollTop = listRef.current.scrollHeight;
    }
  }, [messages]);

  function sendMessage() {
    if (!text.trim() && !attachment) return;
    const newMsg = {
      id: Date.now(),
      from: "me",
      text: text.trim() || (attachment ? `Sent an attachment: ${attachment.name}` : ""),
      time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      attachment: attachment ? { name: attachment.name, size: attachment.size } : null,
    };
    setMessages((m) => [...m, newMsg]);
    setText("");
    setAttachment(null);
    setShowEmoji(false);
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  function onFileChange(e) {
    const file = e.target.files[0];
    if (file) setAttachment(file);
    // reset input so same file can be picked again if removed
    e.target.value = null;
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <div className="w-full max-w-4xl h-[80vh] bg-white shadow-lg rounded-2xl grid grid-cols-12 overflow-hidden">
        {/* Left: Sidebar */}
        <aside className="col-span-3 border-r p-4 bg-gradient-to-b from-white to-gray-50">
          <div className="flex items-center gap-3 mb-6">
            <div className="h-12 w-12 rounded-full bg-indigo-500 flex items-center justify-center text-white font-bold">RT</div>
            <div>
              <div className="font-semibold">Raveena</div>
              <div className="text-xs text-gray-500">Online</div>
            </div>
          </div>

          <div className="space-y-2">
            {/** Example contacts */}
            {[
              { id: 1, name: "Asha", last: "See you tomorrow" },
              { id: 2, name: "Vikram", last: "Thanks!" },
              { id: 3, name: "Priya", last: "Sent the file" },
            ].map((c) => (
              <div key={c.id} className="flex items-center gap-3 p-2 rounded-lg hover:bg-gray-100 cursor-pointer">
                <div className="h-10 w-10 rounded-full bg-gray-200 flex items-center justify-center">{c.name[0]}</div>
                <div className="flex-1">
                  <div className="font-medium text-sm">{c.name}</div>
                  <div className="text-xs text-gray-400 truncate">{c.last}</div>
                </div>
                <div className="text-xs text-gray-400">2:15</div>
              </div>
            ))}
          </div>
        </aside>

        {/* Main chat area */}import React, { useState, useRef, useEffect } from "react";
import { PaperPlane, Smile, Paperclip, X } from "lucide-react";

// Default export: ChatUI component
export default function ChatUI() {
  const [messages, setMessages] = useState([
    { id: 1, from: "them", text: "Hey! Welcome to the chat.", time: "11:00 AM" },
    { id: 2, from: "me", text: "Hi — nice UI!", time: "11:01 AM" },
  ]);
  const [text, setText] = useState("");
  const [showEmoji, setShowEmoji] = useState(false);
  const [attachment, setAttachment] = useState(null);
  const listRef = useRef(null);

  useEffect(() => {
    // auto-scroll to bottom when messages change
    if (listRef.current) {
      listRef.current.scrollTop = listRef.current.scrollHeight;
    }
  }, [messages]);

  function sendMessage() {
    if (!text.trim() && !attachment) return;
    const newMsg = {
      id: Date.now(),
      from: "me",
      text: text.trim() || (attachment ? `Sent an attachment: ${attachment.name}` : ""),
      time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
      attachment: attachment ? { name: attachment.name, size: attachment.size } : null,
    };
    setMessages((m) => [...m, newMsg]);
    setText("");
    setAttachment(null);
    setShowEmoji(false);
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  function onFileChange(e) {
    const file = e.target.files[0];
    if (file) setAttachment(file);
    // reset input so same file can be picked again if removed
    e.target.value = null;
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <div className="w-full max-w-4xl h-[80vh] bg-white shadow-lg rounded-2xl grid grid-cols-12 overflow-hidden">
        {/* Left: Sidebar */}
        <aside className="col-span-3 border-r p-4 bg-gradient-to-b from-white to-gray-50">
          <div className="flex items-center gap-3 mb-6">
            <div className="h-12 w-12 rounded-full bg-indigo-500 flex items-center justify-center text-white font-bold">RT</div>
            <div>
              <div className="font-semibold">Raveena</div>
              <div className="text-xs text-gray-500">Online</div>
            </div>
          </div>

          <div className="space-y-2">
            {/** Example contacts */}
            {[
              { id: 1, name: "Asha", last: "See you tomorrow" },
              { id: 2, name: "Vikram", last: "Thanks!" },
              { id: 3, name: "Priya", last: "Sent the file" },
            ].map((c) => (
              <div key={c.id} className="flex items-center gap-3 p-2 rounded-lg hover:bg-gray-100 cursor-pointer">
                <div className="h-10 w-10 rounded-full bg-gray-200 flex items-center justify-center">{c.name[0]}</div>
                <div className="flex-1">
                  <div className="font-medium text-sm">{c.name}</div>
                  <div className="text-xs text-gray-400 truncate">{c.last}</div>
                </div>
                <div className="text-xs text-gray-400">2:15</div>
              </div>
            ))}
          </div>
        </aside>

        {/* Main chat area */}