;; Auto-generated. Do not edit!


(when (boundp 'challenge_1::state)
  (if (not (find-package "CHALLENGE_1"))
    (make-package "CHALLENGE_1"))
  (shadow 'state (find-package "CHALLENGE_1")))
(unless (find-package "CHALLENGE_1::STATE")
  (make-package "CHALLENGE_1::STATE"))

(in-package "ROS")
;;//! \htmlinclude state.msg.html


(defclass challenge_1::state
  :super ros::object
  :slots (_state ))

(defmethod challenge_1::state
  (:init
   (&key
    ((:state __state) "")
    )
   (send-super :init)
   (setq _state (string __state))
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:serialization-length
   ()
   (+
    ;; string _state
    4 (length _state)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _state
       (write-long (length _state) s) (princ _state s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _state
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _state (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get challenge_1::state :md5sum-) "af6d3a99f0fbeb66d3248fa4b3e675fb")
(setf (get challenge_1::state :datatype-) "challenge_1/state")
(setf (get challenge_1::state :definition-)
      "string state
")



(provide :challenge_1/state "af6d3a99f0fbeb66d3248fa4b3e675fb")


