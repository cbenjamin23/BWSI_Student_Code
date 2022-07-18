;; Auto-generated. Do not edit!


(when (boundp 'challenge_1::State)
  (if (not (find-package "CHALLENGE_1"))
    (make-package "CHALLENGE_1"))
  (shadow 'State (find-package "CHALLENGE_1")))
(unless (find-package "CHALLENGE_1::STATE")
  (make-package "CHALLENGE_1::STATE"))

(in-package "ROS")
;;//! \htmlinclude State.msg.html


(defclass challenge_1::State
  :super ros::object
  :slots (_battery _height _pressure ))

(defmethod challenge_1::State
  (:init
   (&key
    ((:battery __battery) 0)
    ((:height __height) 0.0)
    ((:pressure __pressure) 0.0)
    )
   (send-super :init)
   (setq _battery (round __battery))
   (setq _height (float __height))
   (setq _pressure (float __pressure))
   self)
  (:battery
   (&optional __battery)
   (if __battery (setq _battery __battery)) _battery)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:pressure
   (&optional __pressure)
   (if __pressure (setq _pressure __pressure)) _pressure)
  (:serialization-length
   ()
   (+
    ;; uint8 _battery
    1
    ;; float64 _height
    8
    ;; float64 _pressure
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _battery
       (write-byte _battery s)
     ;; float64 _height
       (sys::poke _height (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pressure
       (sys::poke _pressure (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _battery
     (setq _battery (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float64 _height
     (setq _height (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pressure
     (setq _pressure (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get challenge_1::State :md5sum-) "7822bfa23aaf591dc3f18eb434eb6e41")
(setf (get challenge_1::State :datatype-) "challenge_1/State")
(setf (get challenge_1::State :definition-)
      "uint8 battery
float64 height
float64 pressure
")



(provide :challenge_1/State "7822bfa23aaf591dc3f18eb434eb6e41")


