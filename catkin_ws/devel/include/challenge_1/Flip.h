// Generated by gencpp from file challenge_1/Flip.msg
// DO NOT EDIT!


#ifndef CHALLENGE_1_MESSAGE_FLIP_H
#define CHALLENGE_1_MESSAGE_FLIP_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace challenge_1
{
template <class ContainerAllocator>
struct Flip_
{
  typedef Flip_<ContainerAllocator> Type;

  Flip_()
    : direction()  {
    }
  Flip_(const ContainerAllocator& _alloc)
    : direction(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _direction_type;
  _direction_type direction;





  typedef boost::shared_ptr< ::challenge_1::Flip_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::challenge_1::Flip_<ContainerAllocator> const> ConstPtr;

}; // struct Flip_

typedef ::challenge_1::Flip_<std::allocator<void> > Flip;

typedef boost::shared_ptr< ::challenge_1::Flip > FlipPtr;
typedef boost::shared_ptr< ::challenge_1::Flip const> FlipConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::challenge_1::Flip_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::challenge_1::Flip_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::challenge_1::Flip_<ContainerAllocator1> & lhs, const ::challenge_1::Flip_<ContainerAllocator2> & rhs)
{
  return lhs.direction == rhs.direction;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::challenge_1::Flip_<ContainerAllocator1> & lhs, const ::challenge_1::Flip_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace challenge_1

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::challenge_1::Flip_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::challenge_1::Flip_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::challenge_1::Flip_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::challenge_1::Flip_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::challenge_1::Flip_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::challenge_1::Flip_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::challenge_1::Flip_<ContainerAllocator> >
{
  static const char* value()
  {
    return "326e9417def5db9a05a2704a4d8de15e";
  }

  static const char* value(const ::challenge_1::Flip_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x326e9417def5db9aULL;
  static const uint64_t static_value2 = 0x05a2704a4d8de15eULL;
};

template<class ContainerAllocator>
struct DataType< ::challenge_1::Flip_<ContainerAllocator> >
{
  static const char* value()
  {
    return "challenge_1/Flip";
  }

  static const char* value(const ::challenge_1::Flip_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::challenge_1::Flip_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string direction\n"
;
  }

  static const char* value(const ::challenge_1::Flip_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::challenge_1::Flip_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.direction);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Flip_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::challenge_1::Flip_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::challenge_1::Flip_<ContainerAllocator>& v)
  {
    s << indent << "direction: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.direction);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CHALLENGE_1_MESSAGE_FLIP_H
